import sys
import quickjs


def main():

    js_code = sys.stdin.read()

    ctx = quickjs.Context()

    output = []

    def capture(*args):
        output.append(" ".join(map(str, args)))


    ctx.add_callable(
        "py_console_log",
        capture
    )


    ctx.eval("""
    var console = {
        log: function(){
            py_console_log.apply(null, arguments);
        }
    };
    """)


    try:
        ctx.eval(js_code)

    except Exception as e:
        print("Error:", e)
        return


    print("\n".join(output))


if __name__ == "__main__":
    main()