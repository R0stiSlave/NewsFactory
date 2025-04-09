from news.models import Author, Category, Post, Comment
from django.contrib.auth.models import User

#Пользователи и Авторы
if not User.objects.filter(username='author1').exists():
    user1 = User.objects.create_user(username='author1')
else:
    user1 = User.objects.get(username='author1')

if not User.objects.filter(username='author2').exists():
    user2 = User.objects.create_user(username='author2')
else:
    user2 = User.objects.get(username='author2')

if not Author.objects.filter(user=user1).exists():
    author1 = Author.objects.create(user=user1)
else:
    author1 = Author.objects.get(user=user1)

if not Author.objects.filter(user=user2).exists():
    author2 = Author.objects.create(user=user2)
else:
    author2 = Author.objects.get(user=user2)

#Категории
cat1, _ = Category.objects.get_or_create(name='Политика')
cat2, _ = Category.objects.get_or_create(name='Экономика')
cat3, _ = Category.objects.get_or_create(name='Спорт')
cat4, _ = Category.objects.get_or_create(name='Образование')

#Посты
post1, _ = Post.objects.get_or_create(
    author=author1,
    post_type='article',
    title='Первая статья',
    defaults={'content': 'Содержание первой статьи'}
)
post1.categories.set([cat1, cat2])

post2, _ = Post.objects.get_or_create(
    author=author2,
    post_type='article',
    title='Вторая статья',
    defaults={'content': 'Содержание второй статьи'}
)
post2.categories.set([cat3])

post3, _ = Post.objects.get_or_create(
    author=author1,
    post_type='news',
    title='Новость дня',
    defaults={'content': 'Свежая новость'}
)
post3.categories.set([cat4, cat2])

#Комментарии
Comment.objects.get_or_create(post=post1, user=user2, content='Супер статья')
Comment.objects.get_or_create(post=post1, user=user1, content='Спасибо')
Comment.objects.get_or_create(post=post2, user=user1, content='Интересненько')
Comment.objects.get_or_create(post=post3, user=user2, content='Not Bad')

# --- Лайки/дизлайки ---
post1.like()
post1.like()
post2.like()
post3.dislike()

for comment in Comment.objects.all():
    comment.like()

# --- Обновление рейтинга ---
author1.update_rating()
author2.update_rating()

# --- Лучший пользователь ---
best_author = Author.objects.order_by('-rating').first()
print(best_author.user.username, best_author.rating)

#Лучшая статья
best_post = Post.objects.order_by('-rating').first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

#Комментарии к лучшей статье
for comment in Comment.objects.filter(post=best_post):
    print(comment.created_at, comment.user.username, comment.rating, comment.content)