import streamlit as st

# List of 10 random YouTube video links and their titles for testing
videos = [
    {"title": "Understanding ADHD - A Parent's Guide", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    {"title": "How to Manage ADHD in Children", "url": "https://www.youtube.com/watch?v=J---aiyznGQ"},
    {"title": "ADHD Symptoms and Treatment Options", "url": "https://www.youtube.com/watch?v=3JZ_D3ELwOQ"},
    {"title": "Strategies for Parenting Children with ADHD", "url": "https://www.youtube.com/watch?v=5qap5aO4i9A"},
    {"title": "ADHD Diagnosis and Support", "url": "https://www.youtube.com/watch?v=LSqgMm0OwYw"},
    {"title": "Living with ADHD: Tips for Parents", "url": "https://www.youtube.com/watch?v=HcdBfQkk9so"},
    {"title": "ADHD Treatment: What Works?", "url": "https://www.youtube.com/watch?v=Fw7HfP-64Z8"},
    {"title": "How ADHD Affects Learning and Behavior", "url": "https://www.youtube.com/watch?v=9bZkp7q19f0"},
    {"title": "Understanding ADHD and Anxiety in Kids", "url": "https://www.youtube.com/watch?v=eVbVzpWwXQ0"},
    {"title": "Parenting Techniques for Kids with ADHD", "url": "https://www.youtube.com/watch?v=kXYiU_JCYtU"}
]

# Function to get YouTube video thumbnail URL
def get_video_thumbnail(url):
    video_id = url.split("v=")[-1]  # Extract video ID from URL
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

# Streamlit app template
def main():
    st.title("ADHD Parent Education")
    st.write("Welcome to the ADHD Parent Education portal! Here are 10 random YouTube videos that can help you understand ADHD better.")

    # Display each video
    for video in videos:
        st.write(f"#### {video['title']}")
        
        # Get the video thumbnail URL
        thumbnail_url = get_video_thumbnail(video['url'])
        
        # Show video thumbnail
        st.image(thumbnail_url, use_column_width=True, caption="Click to Watch")

        # Embed the YouTube video using st.video
        st.video(video['url'])

    # Add copyright notice at the bottom
    st.write("\n")
    st.write("All copyrights reserved to Dr. Shurtika Khairnar 2024")

# Run the Streamlit app
if __name__ == "__main__":
    main()
