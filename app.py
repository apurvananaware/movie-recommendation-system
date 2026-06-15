import streamlit as st
import pickle

# Page Configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #FF4B4B;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #B0B0B0;
    margin-bottom: 30px;
}

.recommendation-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1E1E1E;
    margin-bottom: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Load Files
movie_pivot = pickle.load(open('movie_list.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie_name):

    movie_index = movie_pivot.index.get_loc(movie_name)

    distances = similarity_scores[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(movie_pivot.index[movie[0]])

    return recommendations

# Sidebar
st.sidebar.title("🎬 About")
st.sidebar.info(
    """
    Movie Recommendation System
    
    Built using:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit
    
    Dataset:
    MovieLens Dataset
    """
)

# Main Heading
st.markdown(
    "<div class='title'>🎬 Movie Recommendation System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Discover movies similar to your favorites</div>",
    unsafe_allow_html=True
)

# Movie Selection
selected_movie = st.selectbox(
    "🔍 Search or Select a Movie",
    movie_pivot.index
)

# Button
if st.button("✨ Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.markdown("## 🍿 Recommended For You")

    for movie in recommendations:
        st.markdown(
            f"<div class='recommendation-box'>🎥 {movie}</div>",
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.caption("Thank You ❤️ ")