package com.example.xinchangli.myapplication;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        new LongOperation().execute("");


    }

    private class LongOperation extends AsyncTask<String, Void, String> {

        @Override
        /**
         Make network connection;
         !!!!(need to change ip address in URL everytime)!!!!
         Get message from Server
         */
        protected String doInBackground(String... params) {
            try {

                URL url = new URL("http://10.20.86.21:5000/");// my IPv4 Address, one may need to change
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setRequestProperty("Accept", "application/json");

                System.out.println(conn.getResponseCode());
                if (conn.getResponseCode() != 200) {
                    throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                }

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));

                String output = br.readLine();
                conn.disconnect();
                return output;
                /**String output;
                System.out.println("Output from Server .... \n");
                while ((output = br.readLine()) != null) {
                    editText.setText(output);
                }*/
            } catch (MalformedURLException e) {

                e.printStackTrace();

            } catch (IOException e) {

                e.printStackTrace();

            }
            return "error";
        }

        @Override
        /**
         Update UI;
         Recieve the return value from  doinbackground() as parameter result

         */
        protected void onPostExecute(String result) {
            TextView txt = findViewById(R.id.textView);
            txt.setText(result);

        }

        @Override
        protected void onPreExecute() {}

        @Override
        protected void onProgressUpdate(Void... values) {}
    }

}
