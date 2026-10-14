import http.server
import json
import os
import sys

PORT = 3456
TARGET_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CURRICULUM_TRACKER.md")

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
            completed_count = 0
            if os.path.exists(TARGET_FILE):
                with open(TARGET_FILE, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("- [x]") or line.strip().startswith("- [X]"):
                            completed_count += 1
            payload = json.dumps({"status": "active", "file": "CURRICULUM_TRACKER.md", "completed": completed_count})
            self.wfile.write(payload.encode("utf-8"))
        elif self.path == "/read":
            if os.path.exists(TARGET_FILE):
                with open(TARGET_FILE, "r", encoding="utf-8") as f:
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
        if self.path == "/sync":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                with open(TARGET_FILE, "w", encoding="utf-8") as f:
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
    print(f"Sync bridge running on http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
