import http.server
import json
import os
import sys

PORT = 3456
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CURRICULUM_FILE = os.path.join(BASE_DIR, "CURRICULUM_TRACKER.md")
PARENT_DIR = os.path.dirname(BASE_DIR)
TASKS_FILE = os.path.join(PARENT_DIR, "TASKS.md")
if not os.path.exists(TASKS_FILE):
    TASKS_FILE = os.path.join(BASE_DIR, "TASKS.md")

class SyncHandler(http.server.BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path in ["/", "/status"]:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            curriculum_done = 0
            if os.path.exists(CURRICULUM_FILE):
                with open(CURRICULUM_FILE, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("- [x]") or line.strip().startswith("- [X]"):
                            curriculum_done += 1
            tasks_done = 0
            if os.path.exists(TASKS_FILE):
                with open(TASKS_FILE, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("- [x]") or line.strip().startswith("- [X]"):
                            tasks_done += 1
            payload = json.dumps({
                "status": "active",
                "curriculum_completed": curriculum_done,
                "tasks_completed": tasks_done
            })
            self.wfile.write(payload.encode("utf-8"))

        elif self.path == "/read-tasks":
            if os.path.exists(TASKS_FILE):
                with open(TASKS_FILE, "r", encoding="utf-8") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/markdown; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

        elif self.path == "/read":
            if os.path.exists(CURRICULUM_FILE):
                with open(CURRICULUM_FILE, "r", encoding="utf-8") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/markdown; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        if self.path == "/sync-tasks":
            try:
                with open(TASKS_FILE, "w", encoding="utf-8") as f:
                    f.write(body)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"success": true, "message": "Updated TASKS.md"}')
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

        elif self.path == "/sync":
            try:
                with open(CURRICULUM_FILE, "w", encoding="utf-8") as f:
                    f.write(body)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"success": true, "message": "Updated CURRICULUM_TRACKER.md"}')
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), SyncHandler)
    print(f"Sync bridge running on http://127.0.0.1:{PORT} for CURRICULUM_TRACKER.md and TASKS.md")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
