#!/usr/bin/env python3

import sys
import json
import urllib.request
import urllib.error

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = response.read()
                return json.loads(data)
            else:
                print(f"Error: HTTP {response.status}")
                return None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Usuario '{username}' no encontrado.")
        else:
            print(f"❌ Error al acceder a la API de GitHub: {e}")
        return None
    except urllib.error.URLError as e:
        print(f"❌ Error de conexión: {e}")
        return None

def parse_event(event):
    type = event.get("type")
    repo = event["repo"]["name"]

    if type == "PushEvent":
        commits = len(event["payload"].get("commits", []))
        return f"📌 Pushed {commits} commit(s) to {repo}"
    elif type == "IssuesEvent":
        action = event["payload"].get("action")
        return f"🐛 {action.capitalize()} an issue in {repo}"
    elif type == "WatchEvent":
        return f"⭐ Starred {repo}"
    elif type == "ForkEvent":
        return f"🍴 Forked {repo}"
    elif type == "PullRequestEvent":
        action = event["payload"].get("action")
        return f"🔀 {action.capitalize()} a pull request in {repo}"
    else:
        return f"🔸 {type} in {repo}"

def main():
    if len(sys.argv) != 2:
        print("Uso: github-activity <nombre-de-usuario>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_github_activity(username)

    if events:
        print(f"\nActividad reciente de @{username}:\n")
        for event in events[:10]:  # Mostramos solo las 10 más recientes
            print("- " + parse_event(event))

if __name__ == "__main__":
    main()
