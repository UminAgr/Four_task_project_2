from rest_framework import serializers
from .models import Category, Branch, Contact, Course


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['value', 'choice']


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class CourseSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    contact = ContactSerializers(many=True, source='contact_set')
    branch = BranchSerializers(many=True, source='branch_set')

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'category', 'contact', 'branch']

        def create(self, validated_data):
            categories_data = validated_data.pop("category")
            contacts_data = validated_data.pop("contact_set")
            branches_data = validated_data.pop("branch_set")
            category = Category.objects.create(**categories_data)
            course = Course.objects.create(**validated_data, category=category)

            for contact_data in contacts_data:
                Contact.objects.create(course=course, **contact_data)
            for branch_data in branches_data:
                Branch.objects.create(course=course, **branch_data)

            return course
