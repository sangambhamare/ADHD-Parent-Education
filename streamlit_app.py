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

# Streamlit app template
def main():
    st.title("ADHD Parent Education")
    st.write("Welcome to the ADHD Parent Education portal! Here are 10 random YouTube videos that can help you understand ADHD better.")

    # Create columns for grid layout
    cols = st.columns(2)  # Two columns for better layout

    # Display each video in a grid layout
    for i, video in enumerate(videos):
        col = cols[i % 2]  # Alternate between the two columns
        
        with col:
            st.write(f"#### {video['title']}")
            
            # Embed YouTube video directly using the URL
            youtube_embed_url = video['url'].replace("watch?v=", "embed/")
            
            # Embed the YouTube video using st.video
            st.video(youtube_embed_url)

    # Add copyright notice at the bottom
    st.write("\n")
    st.write("All copyrights reserved to Dr. Shurtika Khairnar 2024")

# Run the Streamlit app
if __name__ == "__main__":
    main()
