def my_function(title, description):
  video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
  return video


def like(dictionary):
  if "likes" in dictionary.keys():
    dictionary["likes"] = +1

    return dictionary


def dislike(dictionary):
  if "dislikes" in dictionary.keys():
    dictionary["dislikes"] = +1

    return dictionary


def add_comment(video, username, comment_text):
  if "comments" in video.keys():
    video["comments"][username] = comment_text

    return video

a = my_function("h", "g")
like(a)
dislike(a)
print(a) 