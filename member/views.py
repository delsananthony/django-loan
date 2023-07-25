from django.shortcuts import redirect, render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
)
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer

from .forms import MemberForm


class MemberAPIVIew(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return the queryset for YourModel
        return Member.objects.all()

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)


def index(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            middlename = form.cleaned_data["middlename"]

            Member.objects.create(
                firstname=firstname, lastname=lastname, middlename=middlename
            )
            # Process the form data
            # Redirect or render a success page
            return redirect("member-list")
    else:
        form = MemberForm()

    return render(request, "member/member.html", {"form": form})


@api_view(["GET"])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def members(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)
