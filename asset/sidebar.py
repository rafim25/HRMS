"""
assets/sidebar.py
"""

from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Assets")
IMG_SRC = "images/ui/assets.svg"

SUBMENUS = [
    {
        "menu": trans("Dashboard"),
        "redirect": reverse("asset-dashboard"),
        "accessibility": "asset.sidebar.dashboard_accessibility",
    },
    {
        "menu": trans("Asset View"),
        "redirect": reverse("asset-category-view"),
        "accessibility": "asset.sidebar.dashboard_accessibility",
    },
    {
        "menu": trans("Asset Batches"),
        "redirect": reverse("asset-batch-view"),
        "accessibility": "asset.sidebar.lot_accessibility",
    },
    {
        "menu": trans("Request and Allocation"),
        "redirect": reverse("asset-request-allocation-view"),
    },
    {
        "menu": trans("Asset History"),
        "redirect": reverse("asset-history"),
        "accessibility": "asset.sidebar.history_accessibility",
    },
]


def dashboard_accessibility(request, submenu, user_perms, *args, **kwargs):
    """
    Determine if the user has the necessary permissions to access the
    dashboard and asset category view.
    """
    return request.user.has_perm("asset.view_assetcategory")


def history_accessibility(request, submenu, user_perms, *args, **kwargs):
    """
    Determine if the user has the necessary permissions to access the
    dashboard and asset category view.
    """
    return request.user.has_perm("asset.view_assetassignment")


def lot_accessibility(request, subment, user_perms, *args, **kwargs):
    """
    Asset batch sidebar accessibility method
    """
    return request.user.has_perm("asset.view_assetlot")