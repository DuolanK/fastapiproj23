from fastapi import FastAPI, Body
from schemas import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT

posts = [
    {
        "id": 1,
        "title": "Toyota GR Supra",
        "text": "The fifth-generation GR Supra, the first global Toyota GAZOO Racing model, represents a 50+ year lineage of unique Toyota sports and GT cars."
    },
    {
        "id": 2,
        "title": "Honda NSX",
        "text": "The Honda NSX, marketed in North America as the Acura NSX, is a two-seat, mid-engined coupe sports car manufactured by Honda. The origins of the NSX trace back to 1984, with the HP-X (Honda Pininfarina eXperimental) concept, which was a mid-engine 3.0 L V6 engine rear wheel drive sports car."
    },
    {
        "id": 3,
        "title": "Nissan GTR",
        "text": "The Nissan GT-R (Japanese: 日産・GT-R, Nissan GT-R), is a high-performance sports car and grand tourer produced by Nissan, unveiled in 2007.[3][4][5] It is the successor to the Skyline GT-R, a high performance variant of the Nissan Skyline. Although this car was the sixth-generation model to bear the GT-R name, the model is no longer part of the Nissan Skyline model line up since that name is now reserved for Nissan's luxury-sport vehicles. The GT-R is built on the exclusively-developed Nissan PM platform, which is an enhanced evolution of the Nissan FM platform used in the separate Nissan Skyline luxury car and the Nissan Z sports car. The GT-R abbreviation stands for Gran Turismo–Racing, obtained from the Skyline GT-R."
    }
]

users = []

app = FastAPI()

# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data" : posts}

# Get single post {id}
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id : int):
    if id > len(posts):
        return {
            "error":"Post with this if doesn't exist"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data":post
            }

@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post Added!"
    }

@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details"
        }