def recite(start, take=1):
    nums = {
        "10" : "Ten",
        "9" : "Nine",
        "8" : "Eight",
        "7" : "Seven",
        "6": "Six",
        "5" : "Five",
        "4" : "Four",
        "3" : "Three",
        "2" : "Two",
        "1" : "One",
        "0" : "no"
    }

    lyrics = ["Ten green bottles hanging on the wall,", "Ten green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be nine green bottles hanging on the wall."]
    recite_lyrics = []
    
    for i in range(start, start - take, -1):
        print(i)

        for j in range(0, 4):                        
            lyrics[j] = lyrics[j].replace("Ten", nums[str(i)])
            lyrics[j] = lyrics[j].replace("nine", nums[str(i - 1)].lower())
            print(lyrics[j])

            recite_lyrics.append(lyrics[j])
            lyrics[j] = lyrics[j].replace(nums[str(i)], "Ten")
            lyrics[j] = lyrics[j].replace(nums[str(i - 1)].lower(), "nine")
        recite_lyrics.append("")

    for index, lyric in enumerate(recite_lyrics):
        if "one" in lyric:
            recite_lyrics[index] = lyric.replace("bottles", "bottle")

        if "One" in lyric:
            recite_lyrics[index] = lyric.replace("bottles", "bottle")
    
        if "if no" in lyric:
            recite_lyrics[index] = lyric.replace("no", "one")

    recite_lyrics.pop()

    return recite_lyrics

if __name__ == "__main__":
    print(recite(3, 3)) #["Ten green bottles hanging on the wall,","Ten green bottles hanging on the wall,","And if one green bottle should accidentally fall,","There'll be nine green bottles hanging on the wall.",
    #"","Nine green bottles hanging on the wall,","Nine green bottles hanging on the wall,","And if one green bottle should accidentally fall,","There'll be eight green bottles hanging on the wall.",]