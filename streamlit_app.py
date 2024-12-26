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
    # Apply custom CSS to make the site more appealing for kids
    st.markdown("""
    <style>
    .stApp {
        background-color: #f1f8e9;
    }
    h1 {
        color: #FF4081;
        font-family: 'Comic Sans MS', sans-serif;
    }
    h2 {
        color: #FF4081;
        font-family: 'Comic Sans MS', sans-serif;
    }
    .stButton>button {
        background-color: #FF4081;
        color: white;
        font-size: 20px;
        border-radius: 20px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff80ab;
    }
    .stTextInput>input {
        font-size: 20px;
        padding: 10px;
    }
    .stMarkdown {
        font-family: 'Comic Sans MS', sans-serif;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("ADHD Parent Education")
    st.write("Welcome to the ADHD Parent Education portal! Let's learn together!")

    query = st.text_input("What would you like to learn about ADHD?", placeholder="Enter topic here...")
    
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
            st.write("Oops! No videos found for this topic.")

    # Add copyright notice
    st.write("\n")
    st.write("All copyrights reserved to Dr. Shurtika Khairnar 2024")

# Run the Streamlit app
if __name__ == "__main__":
    main()
