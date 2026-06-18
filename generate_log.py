from lib.generate_log import generate_log, fetch_data

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
