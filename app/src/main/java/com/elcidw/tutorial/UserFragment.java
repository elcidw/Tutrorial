package com.elcidw.tutorial;


import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * A simple {@link Fragment} subclass.
 */
public class UserFragment extends Fragment {

    public static final String LOG_TAG = MainActivity.class.getSimpleName();

    /**
     * URL to query the USGS dataset for earthquake information
     */
    private static final String USGS_REQUEST_URL =
            "http://192.168.1.117:8080/users/all";

    public UserFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        final View view = inflater.inflate(R.layout.fragment_user, container, false);

// Instantiate the RequestQueue.


        String url = USGS_REQUEST_URL;


// Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        updateUi(view, response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
//setText("That didn't work!");
            }
        });
// Add the request to the RequestQueue.
        MainActivity.queue.add(stringRequest);
        return view;
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        getActivity().setTitle("EarthQuake Information");
    }

    @Override
    public void onViewStateRestored(@Nullable Bundle savedInstanceState) {
        super.onViewStateRestored(savedInstanceState);
        getActivity().setTitle("EarthQuake Information");
    }

    /**
     * Update the screen to display information from the given {@link Event}.
     */
    private void updateUi(View view, String userJSON) {
        // Display the earthquake title in the UI

        try {
            //   JSONObject baseJsonResponse = new JSONObject(userJSON);
            JSONArray userArray = new JSONArray(userJSON);

            // If there are results in the features array
            if (userArray.length() > 0) {
                // Extract out the first feature (which is an earthquake)
                JSONObject user = userArray.getJSONObject(1);
                //        JSONObject properties = firstFeature.getJSONObject("properties");

                // Extract out the title, time, and tsunami values//
                String userid = user.getString("id");
                String username = user.getString("name");
                String useremail = user.getString("email");

                TextView idTextView = view.findViewById(R.id.userid);
                idTextView.setText(userid);

                // Display the earthquake date in the UI
                TextView nameTextView = view.findViewById(R.id.username);
                nameTextView.setText(username);

                // Display whether or not there was a tsunami alert in the UI
                TextView emailTextView = view.findViewById(R.id.useremail);
                emailTextView.setText(useremail);

            }
        } catch (JSONException e) {
            Log.e(LOG_TAG, "Problem parsing the earthquake JSON results", e);
//                return new Event(userJSON,10000002000030L,1);
        }


    }


}
