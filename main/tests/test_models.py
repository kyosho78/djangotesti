import pytest
from django.contrib.auth.models import User
from main.models import Post

@pytest.mark.django_db
def test_post_creation():
    user = User.objects.create_user(username='testuser', password='password')
    post = Post.objects.create(content="This is a test post.", author=user)
    
    assert post.content == "This is a test post."
    assert post.author.username == 'testuser'