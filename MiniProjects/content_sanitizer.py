# Sample posts (List Processing)
posts = [
    "User101: I absolutely hate this useless update http://fakeupdate.com",
    "User202: This platform is amazing and helpful",
    "User303: Such a toxic and bad environment, I hate it http://dangerlink.com",
    "User404: Nothing bad here just learning and growing",
    "User101: I hate hate hate this feature it's so toxic",
    "User505: Visit this now http://clickbait.com it's not bad at all",
    "User606: This is a bad example of a toxic system",
    "User707: Clean content with no issues at all",
    "User808: I totally HATE this thing (case insensitive check)",
    "User909: badbad words should still be detected properly"
]

banned_words = ["bad", "toxic", "hate"]

user_flags = {
    "User123": 0,
    "User456": 0,
    "User789": 0
}

total_posts = len(posts)
cleaned_posts = 0
blocked_posts = 0
links = []
safe_posts = []
for post in posts:
    words = post.split()
    new_post = []
    has_banned = False

    for word in words:
        # Link Extraction
        if word.startswith("http"):
            links.append(word)
        clean_word = word
        for banned in banned_words:
            if banned in word.lower():
                clean_word = "***"
                has_banned = True

        new_post.append(clean_word)

    cleaned_text = " ".join(new_post)
    safe_posts.append(cleaned_text)
    if has_banned:
        cleaned_posts += 1
        username = post.split(":")[0]
        if username not in user_flags:
           user_flags[username] = 0
        user_flags[username] += 1
    else:
        blocked_posts += 1

with open("links_found.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

print("---- CLEANED POSTS ----")
for p in safe_posts:
    print(p)

print("\n---- REPORT ----")
print("Total Posts Screened:", total_posts)
print("Cleaned:", cleaned_posts)
print("Clean:", blocked_posts)

print("\n---- USER FLAGS ----")
for user, count in user_flags.items():
    print(user, "flagged:", count)