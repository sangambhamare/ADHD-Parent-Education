import streamlit as st
import pandas as pd
from googleapiclient.discovery import build

# Function to get YouTube videos based on a search query
def get_youtube_videos(query, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=5
    )
    response = request.execute()

    video_list = []
    for item in response.get("items", []):
        video = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
        }
        video_list.append(video)

    return pd.DataFrame(video_list)

# Main function for Streamlit app
def main():
    st.title("ADHD Parent Education")
    st.write("Welcome to the ADHD Parent Education portal!")

    query = st.text_input("Enter a search topic related to ADHD:")
    
    if query:
        api_key = "YOUR_YOUTUBE_API_KEY"  # Replace with your API key
        st.write("Fetching related YouTube videos...")
        videos_df = get_youtube_videos(query, api_key)

        if not videos_df.empty:
            st.write(f"### Related Videos for: {query}")
            for _, row in videos_df.iterrows():
                st.write(f"#### {row['title']}")
                st.write(f"Description: {row['description']}")
                st.write(f"[Watch here]({row['url']})")
        else:
            st.write("No videos found for the given query.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
