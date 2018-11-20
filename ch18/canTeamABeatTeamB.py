
import collections

def canTeamABeatTeamB(matches, teamA, teamB):
    def buildGraph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winningTeam].add(match.losingTeam)
        return graph

    def isReachableDFS(graph, cur, dst, visited=set()):
        if cur == dst:
            return True
        elif cur in visited or cur not in graph:
            return False

        visited.add(cur)

        return any(isReachableDFS(graph, team, dst) for team in graph[cur])

    return isReachableDFS(buildGraph(), teamA, teamB)
