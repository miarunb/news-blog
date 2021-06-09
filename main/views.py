from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreatePostForm, UpdatePostForm
from .models import Category, Post


#TODO: Переписать при помощи классов

#class IndexPage(View):
    #def get(self, request):
        #categories = Category.objects.all()
        #return render(request, 'main/index.html', {'categories': categories})

class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'
# posts/category_id/
# posts/?categoty=id
class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)

class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'
    context_object_name = 'post'

class CreateNewPostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm

class EditPostView(UpdateView):
    queryset = Post.objects.all()
    template_name ='main/edit_post.html'
    form_class = UpdatePostForm

class DeletePostView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'

#TODO: Смена и восстанавление пароля
#TODO: Создание, редактирование и удаление постов
#TODO: HTML - письмо
#TODO: Фильтрация, поиск, сортировка
#TODO: Пагинация
#TODO: Переиспользование шаблонов
#TODO: Проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: Описание (README)
