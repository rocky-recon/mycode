#!/usr/bin/python3


from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#@app.route("/groups", methods =["POST", "GET"])



#groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
#          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
#          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]
@app.route("/<groups>")
def index(groups):
    return render_template("jinja2_groups.html", name = groups)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) #runs the application
