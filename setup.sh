mkdir -p ~/.streamlit/

echo "\
[server]\n\
address = 0.0.0.0\n\
enableCORS = false\n\
headless = true\n\
" > ~/.streamlit/config.toml
