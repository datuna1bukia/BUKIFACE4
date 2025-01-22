from chemiko import app  # Import the app directly
from chemiko import create_admin
from chemiko.routes import home,about,register,login,logout,save_picture,account,new_post,post,update_post,delete_post,user_posts,admin,delete_post_user,delete_user
if __name__ == '__main__':
    create_admin()
    app.run(debug=True,host = "0.0.0.0")
