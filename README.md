
# News Portal - README

## Как запустить проект

1. Убедитесь, что у вас установлен Python и Django.
2. Клонируйте репозиторий на свой локальный компьютер:
   ```bash
   git clone <url-репозитория>
   ```
3. Перейдите в директорию проекта:
   ```bash
   cd <название_проекта>
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Примените миграции:
   ```bash
   python manage.py migrate
   ```

6. Создайте суперпользователя (если ещё не сделали):
   ```bash
   python manage.py createsuperuser
   ```

## Как работать с Django Shell

Для работы с Django Shell вам нужно будет запустить интерактивную оболочку Django:

```bash
python manage.py shell
```

После этого в консоли будет доступна возможность взаимодействовать с моделями Django, выполнять запросы и манипулировать данными в базе.

### Пример команд в Django Shell

1. **Создание пользователей и авторов**

   В Django Shell создайте пользователей и авторов. Пример команд:
   ```python
   from django.contrib.auth.models import User
   from myapp.models import Author

   user1 = User.objects.create_user(username='author1', password='password123')
   user2 = User.objects.create_user(username='author2', password='password123')

   author1 = Author.objects.create(user=user1)
   author2 = Author.objects.create(user=user2)
   ```

2. **Создание категорий**
   
   Для добавления категорий в систему:
   ```python
   from myapp.models import Category

   category1 = Category.objects.create(name='Политика')
   category2 = Category.objects.create(name='Спорт')
   ```

3. **Создание постов**

   Для создания постов и назначения категорий:
   ```python
   from myapp.models import Post

   post1 = Post.objects.create(
       author=author1,
       post_type='article',
       title='Первая статья',
       content='Содержание первой статьи'
   )
   post1.categories.add(category1, category2)

   post2 = Post.objects.create(
       author=author2,
       post_type='news',
       title='Новость дня',
       content='Содержание новости'
   )
   post2.categories.add(category2)
   ```

4. **Создание комментариев**

   Пример добавления комментариев:
   ```python
   from myapp.models import Comment
   from django.contrib.auth.models import User

   user3 = User.objects.create_user(username='commenter', password='password123')

   Comment.objects.create(post=post1, user=user3, content='Отличная статья!')
   ```

5. **Применение методов `like()` и `dislike()`**

   Пример лайков и дизлайков:
   ```python
   post1.like()
   post2.dislike()
   ```

6. **Обновление рейтингов авторов**

   Для обновления рейтинга авторов:
   ```python
   author1.update_rating()
   author2.update_rating()
   ```

7. **Получение лучшего пользователя**

   Для вывода информации о лучшем пользователе по рейтингу:
   ```python
   best_author = Author.objects.order_by('-rating').first()
   print(best_author.user.username, best_author.rating)
   ```

8. **Получение лучшей статьи**

   Для вывода информации о лучшей статье:
   ```python
   best_post = Post.objects.order_by('-rating').first()
   print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())
   ```

9. **Вывод всех комментариев к лучшей статье**

   Для вывода комментариев к лучшей статье:
   ```python
   for comment in Comment.objects.filter(post=best_post):
       print(comment.created_at, comment.user.username, comment.rating, comment.content)
   ```
