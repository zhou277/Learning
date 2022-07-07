from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peppy"]
graph["alice"] = ["peppy"]
graph["anun"] = []
graph["peppy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """通过判断结尾是不是m来决定是不是需要找的结果"""
    return name[-1] == 'm'


def search(name):
    search_queue = deque() // "使用deque创建一个队列"
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + "He is seller")
            return True
        else:
            search_queue += graph[person] // "不检查已经检查过的人"
            searched.append(person)
    return False


search("you")
