
def breakingRecords(scores) -> list[int]:
    # init vals
    min_rec = scores[0]
    max_rec = scores[0]
    records = [0, 0]  # Index 0 = breaking most points records | index 1 = breaking least points records
    for i in range(len(scores)):
        score = scores[i]
        if score > max_rec:
            max_rec = score
            records[0] += 1
        if score < min_rec:
            min_rec = score
            records[1] += 1

    return records


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
breakingRecords(scores)
