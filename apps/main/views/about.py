from rest_framework import generics
from rest_framework.views import APIView, Response

from apps.main.models import AboutUs, CompanyCertificate, Certificate, SocialMedia, Contact
from apps.main.serializers.about import (
    AboutUsSerializer,
    CompanyCertificateSerializer,
    CertificateListSerializer,
    SocialMediaListSerializer,
    ContactListSerializer,
)


class AboutUsView(APIView):
    def get(self, obj):
        queryset = AboutUs.objects.filter(active=True).first()
        serializer = AboutUsSerializer(queryset)
        return Response(serializer.data)


class CompanyCertificateView(APIView):
    def get(self, obj):
        queryset = CompanyCertificate.objects.filter(active=True).first()
        serializer = CompanyCertificateSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.filter(active=True)
    serializer_class = CertificateListSerializer


class SocialMediaListView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaListSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
