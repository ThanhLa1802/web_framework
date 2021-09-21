from .extension import ma
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')
class CatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
class BorrowSchema(ma.Schema):
    class Meta:
        fields = ('id', 'book_id','student_id','borrow_date', 'return_date')
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'page_count', 'author_id', 'category_id')

