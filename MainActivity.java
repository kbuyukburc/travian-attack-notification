package com.example.kbuyu.tracer;
import android.app.Service;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import com.google.firebase.iid.FirebaseInstanceId;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.google.firebase.messaging.FirebaseMessaging;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String token = FirebaseInstanceId.getInstance().getToken();

        // Log and toast

        Log.d("token",token);
        Toast.makeText(MainActivity.this, token, Toast.LENGTH_SHORT).show();

        //start
        //Intent intent = new Intent(getApplicationContext(),MyFirebaseMessagingService.class);
        //startService(intent);//Servisi başlatır
    }

}
