package com.apextax.practicehub;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(ApexHardwarePlugin.class);
        super.onCreate(savedInstanceState);
    }
}
