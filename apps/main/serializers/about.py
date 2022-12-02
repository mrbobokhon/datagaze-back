from rest_framework import serializers

from apps.main.models.about import AboutUs, CompanyCertificate, Certificate, SocialMedia, Contact


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("title", "sub_title")


class CompanyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCertificate
        fields = ("certificate", "title", "sub_title", "text")


class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("image",)


class SocialMediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("icon", "link")


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("icon", "contact")
