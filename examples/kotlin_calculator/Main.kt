import java.util.function.BinaryOperator

enum class IntOperator(val symbol: String) : BinaryOperator<Int> {
    PLUS("+") {
        override fun apply(t: Int, u: Int) = t + u
    },
    MINUS("-") {
        override fun apply(t: Int, u: Int) = t - u
    },
    MULTIPLY("*") {
        override fun apply(t: Int, u: Int) = t * u
    },
    DIVIDE("/") {
        override fun apply(t: Int, u: Int) = t / u
    };

    companion object {
        fun possibleSymbols() = IntOperator.values().map { it.symbol }

        fun bySymbol(symbol: String) = IntOperator.values().firstOrNull { it.symbol == symbol }
    }
}


fun <T> readInput(errorMessage: String, inputConverter: (String) -> T?): T {
    do {
        val input: T? = inputConverter(readln())
        input?.run { return this }
        println(errorMessage)
    } while (true)
}


fun main() {
    println("Welcome to a simple Kotlin calculator!\n")

    do {
        print("Please enter the operator (possible values: ${IntOperator.possibleSymbols().joinToString(", ")}): ")
        val operator = readInput(
            "Incorrect operator. Possible values: ${IntOperator.possibleSymbols().joinToString(", ")}.",
        ) { IntOperator.bySymbol(it) }

        println()

        print("Please enter the left operand: ")
        val leftOperand = readInput("Incorrect operand. It must be an integer.") { it.toIntOrNull() }

        println()

        print("Please enter the right operand: ")
        val rightOperand = readInput("Incorrect operand. It must be an integer.") { it.toIntOrNull() }

        println()

        println("$leftOperand ${operator.symbol} $rightOperand = ${operator.apply(leftOperand, rightOperand)}\n")
    } while (true)
}
