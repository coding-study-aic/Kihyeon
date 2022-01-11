class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()

        for(t in commands){
            val i = t[0]-1
            val j = t[1]-1
            val k = t[2]-1
            answer = answer.plus(array.slice(i..(j)).sorted()[k])
        }

        return answer
    }
}