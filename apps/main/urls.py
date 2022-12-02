from django.urls import path

from .views.about import AboutUsView, CompanyCertificateView, CertificateListView, SocialMediaListView, ContactListView
from .views.home import MenuListView, SliderListView, StatisticListView, PartnerListView

# home page apis
urlpatterns = [
    path("menus/", MenuListView.as_view(), name="menu_list"),
    path("sliders/", SliderListView.as_view(), name="slider_list"),
    path("statistics/", StatisticListView.as_view(), name="statistic_list"),
    path("parners/", PartnerListView.as_view(), name="partners_list"),
]

# about page apis
urlpatterns += [
    path("about-us/", AboutUsView.as_view(), name="about_us"),
    path("company-certificate/", CompanyCertificateView.as_view(), name="company_certificate"),
    path("certificates/", CertificateListView.as_view(), name="certificate_list"),
    path("social-medias/", SocialMediaListView.as_view(), name="social_media_list"),
    path("contacts/", ContactListView.as_view(), name="contact_list"),
]
