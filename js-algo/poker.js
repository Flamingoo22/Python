// Your task is to implement an algorithm that is able to execute the Twenty-One Card Trick. To simplify things, the cards will be changed to the set of integers between 1 and 21(inclusive). The function will be passed as argument a member of the audience that has selected a certain card and has a method get_input that receives a list of 3 lists as arguments and returns the index of the row contained the selected card. Example:

// const audience = new Audience(13);

// > audience.getInput([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14], [15,16,17,18,19,20,21]]);
// 1 // Since 13 is at the 2nd row

function intersection (set1, set2) {
    const set3 = new Set();
    for (const elem of set1)
        if (set2.has(elem))
        set3.add(elem);
    return set3;
    }

    function guessTheCard(audience) {
        const cols1 = [ [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21] ];
        const cols2 = [ [1, 2, 3, 8, 9, 15, 16], [4, 5, 10, 11, 12, 17, 18], [6, 7, 13, 14, 19, 20, 21] ];
        const cols3 = [ [1, 4, 7, 10, 13, 16, 19], [2, 5, 8, 11, 14, 17, 20], [3, 6, 9, 12, 15, 18, 21] ];

    const COLS = [cols1, cols2, cols3];
    const sets = COLS.map(
        (cols, i) => new Set(COLS[i][audience.getInput(cols)])
    );
    return intersection(intersection(sets[0], sets[1]), sets[2]).values().next().value;
}