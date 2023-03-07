


# data = [{ id: 1, "video_title" : “science lesson”, tags: [“tech”,”sci-fi”], file_name: “test3.mp4”},
# { id: 2, video_title : “computer engg – embedded systems”, tags: [“computer”,”embedded systems”, “difficult”], file_name: test2.mp4},
# { id: 3, video_title : null, tags: null, file_name: “test.mp4"}]


data = [{'id': 1, "video_title" : "science_lesson", 'tags': ['tech', 'sci_fi'], 'file_name': "test3.mp4"},{'id': 2, "video_title" : "computer engg – embedded systems", 'tags': ["computer", "embedded systems", "difficult"], 'file_name': "test3.mp4"}]


tag = list(map(str, input("Enter your tags").strip().split()))

#find the tags for the data and print video_title and filename

print("Results are as follows for your tag input: ")

for i in range(len(data)):
    for j in range(len(data[0])):
        if tag in data[i]['tags']:
            print("Your video_title is ", data[i]['video_title'])
            print("your file_name is ", data[i]['file_name'])