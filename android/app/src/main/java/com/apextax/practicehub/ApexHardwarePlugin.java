package com.apextax.practicehub;

import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.speech.tts.TextToSpeech;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.util.ArrayList;
import java.util.Locale;

@CapacitorPlugin(name = "ApexHardware")
public class ApexHardwarePlugin extends Plugin implements TextToSpeech.OnInitListener {

    private TextToSpeech tts;
    private SpeechRecognizer speechRecognizer;

    @Override
    public void load() {
        super.load();
        tts = new TextToSpeech(getContext(), this);
    }

    @Override
    public void onInit(int status) {
        if (status == TextToSpeech.SUCCESS) {
            tts.setLanguage(Locale.US);
            tts.setSpeechRate(1.03f);
        }
    }

    @PluginMethod
    public void speakInterviewerPrompt(PluginCall call) {
        String text = call.getString("text");
        if (text == null || text.isEmpty()) {
            call.reject("Missing text");
            return;
        }
        if (tts != null) {
            tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, "INTERVIEW_PROMPT");
        }
        call.resolve();
    }

    @PluginMethod
    public void stopSpeaking(PluginCall call) {
        if (tts != null && tts.isSpeaking()) {
            tts.stop();
        }
        call.resolve();
    }

    @PluginMethod
    public void startInterviewListening(PluginCall call) {
        getActivity().runOnUiThread(() -> {
            if (speechRecognizer == null) {
                speechRecognizer = SpeechRecognizer.createSpeechRecognizer(getContext());
            }
            Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US");
            intent.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true);
            // Extended 3000ms silence tolerance for complex IRC statutory reasoning
            intent.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS, 3000L);
            intent.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_POSSIBLY_COMPLETE_SILENCE_LENGTH_MILLIS, 2500L);

            speechRecognizer.setRecognitionListener(new RecognitionListener() {
                @Override
                public void onPartialResults(Bundle partialResults) {
                    ArrayList<String> matches = partialResults.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
                    if (matches != null && !matches.isEmpty()) {
                        JSObject data = new JSObject();
                        data.put("transcript", matches.get(0));
                        data.put("isFinal", false);
                        notifyListeners("voiceArenaTranscript", data);
                    }
                }

                @Override
                public void onResults(Bundle results) {
                    ArrayList<String> matches = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
                    if (matches != null && !matches.isEmpty()) {
                        JSObject data = new JSObject();
                        data.put("transcript", matches.get(0));
                        data.put("isFinal", true);
                        notifyListeners("voiceArenaTranscript", data);
                    }
                }

                @Override
                public void onReadyForSpeech(Bundle params) {}
                @Override
                public void onBeginningOfSpeech() {}
                @Override
                public void onRmsChanged(float rmsdB) {}
                @Override
                public void onBufferReceived(byte[] buffer) {}
                @Override
                public void onEndOfSpeech() {}
                @Override
                public void onError(int error) {
                    JSObject data = new JSObject();
                    data.put("error", error);
                    notifyListeners("voiceArenaError", data);
                }
                @Override
                public void onEvent(int eventType, Bundle params) {}
            });
            speechRecognizer.startListening(intent);
            call.resolve();
        });
    }

    @PluginMethod
    public void stopInterviewListening(PluginCall call) {
        getActivity().runOnUiThread(() -> {
            if (speechRecognizer != null) {
                speechRecognizer.stopListening();
            }
            call.resolve();
        });
    }
}

