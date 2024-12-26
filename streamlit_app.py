import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
import time

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #fce4ec;
            color: #4A148C;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .title {
            font-size: 48px;
            color: #FF4081;
            text-align: center;
        }
        .header {
            font-size: 30px;
            color: #3F51B5;
        }
        .video-card {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin: 10px 0;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #FF4081;
            margin-top: 20px;
        }
        .emoji {
            font-size: 60px;
        }
        .fun-button {
            background-color: #FF4081;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 20px;
            border-radius: 10px;
            cursor: pointer;
        }
        .fun-button:hover {
            background-color: #F50057;
        }
    </style>
""", unsafe_allow_html=True)

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
    st.markdown('<h1 class="title">🎉 ADHD Parent Education for Kids 🎉</h1>', unsafe_allow_html=True)
    st.write("👦👧 Welcome to a fun learning portal for ADHD! 🎈")

    query = st.text_input("What would you like to learn about? 🤔", placeholder="e.g., ADHD Tips for Kids")

    if query:
        st.markdown('<h2 class="header">Here are some fun videos for you! 🎥</h2>', unsafe_allow_html=True)
        api_key = "YOUR_YOUTUBE_API_KEY"  # Replace with your API key
        st.write("Fetching related YouTube videos... 🧑‍💻")
        videos_df = get_youtube_videos(query, api_key)

        if not videos_df.empty:
            for _, row in videos_df.iterrows():
                st.markdown(f"""
                    <div class="video-card">
                        <h3>{row['title']} 🎬</h3>
                        <p>{row['description']}</p>
                        <a href="{row['url']}" target="_blank">
                            <button class="fun-button">Watch Now! 🚀</button>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.write("Oops! No videos found for the given query 😔")

    st.markdown("<div class='footer'>All copyrights reserved to Dr. Shurtika Khairnar 2024 🌟</div>", unsafe_allow_html=True)

    # Add a fun animation
    st.markdown("""
        <div class="emoji">🦄✨</div>
        <p style="text-align:center;">Enjoy your time learning with us! 💡🌟</p>
    """, unsafe_allow_html=True)

    time.sleep(1)  # Optional to make things feel more dynamic

# Run the Streamlit app
if __name__ == "__main__":
    main()
