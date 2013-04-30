import sys


HTML = """
<?doctype html>
<html>
  <head>
    <style>
body {
  background-color: gray;
}
h1, h2, h3 {
  font-style: italic;
}
h1, h2 {
  float: left;
}
h1 {
  margin-top: 1em;
}
h2 {
  background-color: white;
  padding: 1ex;
  margin: 1ex;
}
table {
  clear: both;
  background-color: white;
  border: solid 2px black;
  border-collapse: collapse;
}
td {
  padding: 20px;
  border: solid 1px black;
  vertical-align: top;
}
.postit {
  float: left;
  background-image: url("Post-it-note.png");
  background-repeat: no-repeat;
  height: 105px;
  width: 99px;
  padding: 20px;

  text-align: center;
  font-weight: bold;
  font-variant: small-caps;
}
.cl {
  clear: left;
}
    </style>
  </head>
  <body>
    <h1>The Business Model Canvas</h1>
    <h2>Designed for: %%s</h2>
    <h2>Designed by: Aur Saraf</h2>
    <table>
      <tr>
	<td rowspan="2">
	  <h3>Key Partners</h3>
          %(partners)s
        </td>
	<td>
	  <h3>Key Activities</h3>
          %(activities)s
        </td>
	<td colspan="2" rowspan="2">
	  <h3>Value Propositions</h3>
          %(values)s
        </td>
	<td>
	  <h3>Customer Relationships</h3>
          %(relationships)s
        </td>
	<td rowspan="2">
	  <h3>Customer Segments</h3>
          %(customers)s
        </td>
      </tr>
      <tr>
	<td>
	  <h3>Key Channels</h3>
          %(channels)s
        </td>
	<td>
	  <h3>Key Resources</h3>
          %(resources)s
	</td>
      </tr>
      <tr>
	<td colspan="3">
	  <h3>Cost Structure</h3>
          %(costs)s
        </td>
	<td colspan="3">
	  <h3>Revenue Streams</h3>
          %(revenues)s
	</td>
      </tr>
    </table>

    <div>
      <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0; float:left" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>
      <h3>Canvas: <a href="http://www.businessmodelcanvas.com">www.businessmodelcanvas.com</a>, Post-It: <a href="http://diskdepot.co.uk">diskdepot.co.uk</a></h3>
      This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
    </div>
  </body>
</html>
"""

POSTIT = '<div class="postit %(classes)s">%(content)s</div>'

CANVAS_CODE = """CANVAS = {
    "customers": [],
    "values": [],
    "channels": [],
    "relationships": [],
    "revenues": [],
    "resources": [],
    "activities": [],
    "partners": [],
    "costs": [],
}
"""


def to_postit(caption):
    classes = ""
    if caption.startswith(" "):
        classes = "cl "
        caption = caption[1:]
    return POSTIT % {"classes": classes, "content": caption}

def write(name, canvas, f):
    canvas = dict((k, "\n".join(map(to_postit, v))) for k, v in canvas.iteritems())
    html = HTML % canvas % name
    f.write(html)

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "-new": 
        with file(sys.argv[2] + ".py", "wb") as f:
            f.write(CANVAS_CODE)
        return 0
    elif len(sys.argv) != 2:
        print "usage: canvas.py name"
        return 1

    name = sys.argv[1]
    module = __import__(name)

    with file(name + ".html", "wb") as f:
        write(name, module.CANVAS, f)

    return 0

if __name__ == '__main__':
    sys.exit(main())