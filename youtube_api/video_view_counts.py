# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import pandas as pd
import json
from pyyoutube import Api

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    clientid = "325283488436-678c3gsbvmkbi9jrnc9iej7ihcsf71i7.apps.googleusercontent.com"
    secret = "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"
    print(clientid, secret)
    api = Api(client_id=clientid.strip(), client_secret=secret.strip())
    api.get_authorization_url()
    api.generate_access_token(authorization_response=str("http://localhost"))
    video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)
    print(video_by_chart.items)


def convert_json_to_table(json_string):
    recs = json_string['items']
    df1 = pd.json_normalize(recs)
    print(df1)
    df1.to_csv("view_counts.csv", sep='\t', encoding='utf-8')


if __name__ == "__main__":
    main()
