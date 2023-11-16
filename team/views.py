from django.shortcuts import render


team_member = [
    {
        "id": 1,
        "name": "Abul Kashem",
        "designation": "Manager",
        "img_path": "img/teams/team-1.jpg"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "designation": "Lead Developer",
        "img_path": "img/teams/team-2.jpg"
    },
    {
        "id": 3,
        "name": "Carlos Rodriguez",
        "designation": "Marketing Specialist",
        "img_path": "img/teams/team-3.jpg"
    },
    {
        "id": 4,
        "name": "Emily Johnson",
        "designation": "Graphic Designer",
        "img_path": "img/teams/team-2.jpg"
    },
    {
        "id": 5,
        "name": "Raj Patel",
        "designation": "Customer Support",
        "img_path": "img/teams/team-1.jpg"
    },
    {
        "id": 6,
        "name": "Sophie Lee",
        "designation": "Finance Analyst",
        "img_path": "img/teams/team-2.jpg"
    },
    {
        "id": 7,
        "name": "Miguel Gonzales",
        "designation": "HR Coordinator",
        "img_path": "img/teams/team-1.jpg"
    },
    {
        "id": 8,
        "name": "Elena Martinez",
        "designation": "Quality Assurance",
        "img_path": "img/teams/team-2.jpg"
    },
]


def team_view(request):

    context = {"teams": team_member}

    return render(request, 'team/teams.html', context)
