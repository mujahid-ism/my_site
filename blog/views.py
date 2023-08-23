from django.shortcuts import render
from .models import Post

# all_posts = [
# 	{
# 		"slug": "mountain-time",
# 		"image": "mountains.jpg",
# 		"author": "John Doe",
# 		"date": "2023-08-21",
# 		"title": "Exploring the Mountain Climbing",
# 		"excerpt": "Discover the beauty of nature through our latest adventure.",
# 		"content": "Join us on an unforgettable journey as we trek through lush forests, across cascading waterfalls, and up rugged mountains."
# 	},
# 	{
# 		"slug": "coding-time",
# 		"image": "coding.jpg",
# 		"author": "Mujahidul Islam",
# 		"date": "2023-08-22",
# 		"title": "Exploring the Software Development",
# 		"excerpt": "Discover the beauty of nature through our latest adventure.",
# 		"content": "Join us on an unforgettable journey as we trek through lush forests, across cascading waterfalls, and up rugged mountains."
# 	},
# 	{
# 		"slug": "wood-time",
# 		"image": "woods.jpg",
# 		"author": "John Smith",
# 		"date": "2023-08-23",
# 		"title": "Exploring the Wood Chopping",
# 		"excerpt": "Discover the beauty of nature through our latest adventure.",
# 		"content": "Join us on an unforgettable journey as we trek through lush forests, across cascading waterfalls, and up rugged mountains."
# 	}
# ]

# Create your views here.
def starting_page(request):
  lattest_sorted_posts = Post.objects.all().order_by('-date')[:3]
  return render(request, 'index.html', {
    'posts': lattest_sorted_posts
	})

def posts(request):
  all_posts = Post.objects.all()
  return render(request, 'all-posts.html', {
    'posts': all_posts
	})

def individual_post(request, slug):
  individual_post = Post.objects.get(slug=slug)
	
  return render(request, 'post-detail.html', {
    'post': individual_post,
    'post_tags': individual_post.post_tags.all()
	})
