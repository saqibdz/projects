class Comment:
  def __init__(self, author, content):
      self.author = author
      self.content = content

  def __str__(self):
      return f"{self.author}: {self.content}"

class Post:
  def __init__(self, title, content, author):
      self.title = title
      self.content = content
      self.author = author
      self.comments = []

  def add_comment(self, author, content):
      comment = Comment(author, content)
      self.comments.append(comment)

  def __str__(self):
      return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"

class Blog:
  def __init__(self, name):
      self.name = name
      self.posts = []
      self.authors = set()

  def create_post(self, title, content, author):
      post = Post(title, content, author)
      self.posts.append(post)
      self.authors.add(author)

  def list_posts(self):
      for post in self.posts:
          print(post)

  def list_comments(self):
      for post in self.posts:
          print(f"Comments for '{post.title}':")
          for comment in post.comments:
              print(comment)

  def __str__(self):
      author_names = [author.name for author in self.authors]
      return f"Blog: {self.name}\nPosts: {len(self.posts)}\nAuthors: {', '.join(author_names)}"

class Author:
  def __init__(self, name):
      self.name = name

  def __str__(self):
      return self.name

def main():
  blog = Blog("My Blog")

  author1 = Author("Alice")
  author2 = Author("Bob")

  blog.create_post("First Post", "This is the content of the first post.", author1)
  blog.create_post("Second Post", "Another exciting post.", author2)

  blog.list_posts()

  blog.posts[0].add_comment("Commenter1", "Great post!")
  blog.posts[0].add_comment("Commenter2", "I learned a lot from this.")

  blog.list_comments()

  print(blog)

if __name__ == "__main__":
  main()
