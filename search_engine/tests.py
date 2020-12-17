import os

from django.core.files import File
from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from category.models import Category
from post.models import Post, MyFileField
from search_engine.views import get_posts_by_query


class CheckSearch(TestCase):
    # Ok, it works

    # Preparing data for testing
    def setUp(self) -> None:
        # print("DEBUG: creating temp materials!")
        with open('file1.txt', 'w') as file1, open('file2.txt', 'w') as file2, open('file3.txt', 'w') as file3:
            file1.write("In general, django.test.TestCase does a full database flush at the start of each new test. "
                        "This means that we do not need to manually delete objects in our tearDown as Chris Pratt has "
                        "mentioned above. The next test setUp will make sure the database is clean.")

            file2.write("I was working on a project that handled some file uploads, and i needed to delete the files "
                        "that were created by the test and the tearDown method was very useful in that situation.")

            file3.write("Finally, in more complicated scenarios, it might also make sense to deliberately persist the "
                        "test database to hunt down specific unit test bugs.")

        category1 = Category.objects.create(text="temp_category1")
        category2 = Category.objects.create(text="temp_category2")
        category3 = Category.objects.create(text='temp_category3')

        category1.save()
        category2.save()
        category3.save()

        attachment1 = MyFileField.objects.create(file=File(open('file1.txt')))
        attachment2 = MyFileField.objects.create(file=File(open('file2.txt')))
        attachment3 = MyFileField.objects.create(file=File(open('file3.txt')))

        attachment1.save()
        attachment2.save()
        attachment3.save()

        post1 = Post.objects.create(
            title="temp_title1",
            who_added='tester-admin',
            author='Shilov-bog',
            date_publication=timezone.now(),

            # it is seen by search engine
            visibility='1',
        )
        post1.attachments.add(attachment1, attachment2)
        post1.categories.add(category1, category2)
        post1.save()

        post2 = Post.objects.create(
            title='temp_title2',
            who_added='tester-admin',
            author='Succi-bog',
            date_publication=timezone.now(),

            # it is seen by search engine
            visibility='1',
        )
        post2.attachments.add(attachment3)
        post2.categories.add(category3)
        post2.save()

        # Removing temp files (they are already saved in good place)
        os.remove('file1.txt')
        os.remove('file2.txt')
        os.remove('file3.txt')

    def test_files_can_be_found_by_titles(self):
        # print("DEBUG: running test_files_can_be_found_by_titles!")
        posts = get_posts_by_query('temp_title1')

        p1 = Post.objects.get(title='temp_title1')
        self.assertEqual(len(posts), 1, msg="Search found more that one objects with the same title")
        self.assertEqual(
            posts[0],
            p1,
            msg=f"The objects are different: obj.id={posts[0].id} should be {p1.id}"
        )

    def test_files_can_be_found_by_categories(self):
        # print("DEBUG: test_files_can_be_found_by_categories!")
        posts = get_posts_by_query('temp_category3')

        p2 = Post.objects.filter(categories__text='temp_category3')

        self.assertEqual(len(posts), 1, msg="Search found more that one objects with the same category")
        self.assertEqual(
            posts[0],
            p2[0],
            msg=f"The objects are different: obj.id={posts[0].id} should be {p2[0].id}"
        )

    def tearDown(self) -> None:
        # print("DEBUG: deleting materials!")
        post1 = Post.objects.get(title='temp_title1')
        post2 = Post.objects.get(title='temp_title2')

        post1.delete()
        post2.delete()

        category1 = Category.objects.get(text='temp_category1')
        category2 = Category.objects.get(text='temp_category2')
        category3 = Category.objects.get(text='temp_category3')

        category1.delete()
        category2.delete()
        category3.delete()
