import sublime
import sublime_plugin
import os
import re
from subprocess import check_output
import operator


class AppCompletions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "keyword.app.bunch"):
            return []

        def trim_App(iter_in):
            result = str(re.sub('.*/([^/]+).app\'', '\\1', str(iter_in)))
            if len(result):
                return result

        all_apps = check_output(['/usr/bin/mdfind', 'kMDItemContentType = "com.apple.application-bundle" && kMDItemDisplayName = "*.app"cd'])

        available_completions = map(trim_App, all_apps.split(b"\n"))

        prefix = prefix.lower()

        out = []
        for comp in available_completions:
            if comp.lower().startswith(prefix):
                out.append(comp)

        return out

class ChainedActionsCommand(sublime_plugin.TextCommand):
    def run(self, edit, actions, args):
        for i, action in enumerate(actions):
            self.view.run_command(action, args[i])

def getFragmentIds(view, name=''):
    frags = []
    frags.extend(view.find_all(r"^(?:-{2,}|[=>#])[\-=># ]*\[([^\]]+)\]", 0))

    regions = frags
    ids = []
    for reg in regions:
        name = view.substr(reg).strip()
        name = str(re.sub('^(?:-{2,}|[=>#])[\\-=># ]*\\[([^\\]]+)\\].*$', '\\1', name))
        ids.append(name)
    return ids

class SnippetFragmentCompletions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "meta.snippet.fragment"):
            return []

        available_completions = getFragmentIds(view)

        prefix = prefix.lower()

        out = []
        for comp in available_completions:
            if comp.lower().startswith(prefix):
                out.append(comp)

        return out
