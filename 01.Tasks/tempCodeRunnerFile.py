data = json.loads(response.text)  # Parse the JSON response

for item in data["items"]:
  # Extract videoId from snippet
  video_id = item["snippet"]["resourceId"]["videoId"]
  # Construct the full YouTube video URL using videoId
  video_url = f"https://www.youtube.com/watch?v={video_id}"
  print(f"Video URL: {video_url}")