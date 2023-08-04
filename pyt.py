import subprocess
import os



# SVN and Git repository URLs
svn_repo_url = "http://20.25.185.244/svn/myrepo/"



# SVN credentials (replace with your actual SVN username and password)
svn_username = "admin"
svn_password = "Prime@123"



# GitHub Personal Access Token (PAT)
github_pat = "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"  # Replace with your GitHub PAT


#os.environ["GIT_ASKPASS"] = "echo"  # Set to "echo" to provide password non-interactively
#os.environ["GITHUB_USERNAME"] = "debjyotimt@gmail.com"  # Replace with your GitHub username
#os.environ["GITHUB_TOKEN"] = github_pat

subprocess.run(["git", "init"])
process = subprocess.Popen(
    ["git", "svn", "init", svn_repo_url, "--no-metadata"],
    stdin=subprocess.PIPE,
    text=True
)
process.communicate(input=f"{svn_username}\n{svn_password}\n")

process = subprocess.Popen(
    ["git", "svn", "fetch", "--username", svn_username],
    stdin=subprocess.PIPE,
    text=True
)
process.communicate(input=svn_password)

print("compile1")
#subprocess.run(["git", "config", "--global", "user.name", "deb2511"])  # Replace with your GitHub username
#subprocess.run(["git", "config", "--global", "user.email", "debjyotimt@gmail.com"])

# Step 2: Add GitHub remote manually (skip repository creation via API)
#github_repo_url = "https://github.com/dmaity2511/svn-github.git"
#ggithub_repo_url = f"https://{gusername}:{gpassword}@github.com/dmaity2511/svn-github.git"
#ithub_repo_url = f"https://{gusername}:{gpassword}@github.com/dmaity2511/svn-github.git"

gusername="deb2511"
gpassword= "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"
github_repo_url = f"https://{gusername}:{gpassword}@github.com/dmaity2511/hiii.git"

subprocess.run(["git", "remote", "add", "origin", github_repo_url])



subprocess.run(["git", "push", "--set-upstream", "origin", "main"])



print("Migration from SVN to Git and GitHub is complete.")
