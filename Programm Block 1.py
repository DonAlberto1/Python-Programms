__enter__(self)
__exit__(self, *args)
__init__(self, host, port=119, user=None, password=None, readermode=None, usenetrc=False, timeout=<object object at 0x00000060CED54C10>)
Initialize an instance.  Arguments:
- host: hostname to connect to
- port: port to connect to (default the standard NNTP port)
- user: username to authenticate with
- password: password to use with username
- readermode: if true, send 'mode reader' command after
              connecting.
- usenetrc: allow loading username and password from ~/.netrc file
            if not specified explicitly
- timeout: timeout (in seconds) used for socket connections
 
readermode is sometimes necessary if you are connecting to an
NNTP server on the local machine and intend to call
reader-specific commands, such as `group'.  If you get
unexpected NNTPPermanentErrors, you might need to set
readermode.
article(self, message_spec=None, *, file=None)
Process an ARTICLE command.  Argument:
- message_spec: article number or message id
- file: filename string or file object to store the article in
Returns:
- resp: server response if successful
- ArticleInfo: (article number, message id, list of article lines)
body(self, message_spec=None, *, file=None)
Process a BODY command.  Argument:
- message_spec: article number or message id
- file: filename string or file object to store the body in
Returns:
- resp: server response if successful
- ArticleInfo: (article number, message id, list of body lines)
capabilities(self)
Process a CAPABILITIES command.  Not supported by all servers.
Return:
- resp: server response if successful
- caps: a dictionary mapping capability names to lists of tokens
(for example {'VERSION': ['2'], 'OVER': [], LIST: ['ACTIVE', 'HEADERS'] })
date(self)
Process the DATE command.
Returns:
- resp: server response if successful
- date: datetime object
debug = set_debuglevel(self, level)
description(self, group)
Get a description for a single group.  If more than one
group matches ('group' is a pattern), return the first.  If no
group matches, return an empty string.
 
This elides the response code from the server, since it can
only be '215' or '285' (for xgtitle) anyway.  If the response
code is needed, use the 'descriptions' method.
 
NOTE: This neither checks for a wildcard in 'group' nor does
it check whether the group actually exists.
descriptions(self, group_pattern)
Get descriptions for a range of groups.
getcapabilities(self)
Get the server capabilities, as read by __init__().
If the CAPABILITIES command is not supported, an empty dict is
returned.
getwelcome(self)
Get the welcome message from the server
(this is read and squirreled away by __init__()).
If the response code is 200, posting is allowed;
if it 201, posting is not allowed.
group(self, name)
Process a GROUP command.  Argument:
- group: the group name
Returns:
- resp: server response if successful
- count: number of articles
- first: first article number
- last: last article number
- name: the group name
head(self, message_spec=None, *, file=None)
Process a HEAD command.  Argument:
- message_spec: article number or message id
- file: filename string or file object to store the headers in
Returns:
- resp: server response if successful
- ArticleInfo: (article number, message id, list of header lines)
help(self, *, file=None)
Process a HELP command. Argument:
- file: Filename string or file object to store the result in
Returns:
- resp: server response if successful
- list: list of strings returned by the server in response to the
        HELP command
ihave(self, message_id, data)
Process an IHAVE command.  Arguments:
- message_id: message-id of the article
- data: file containing the article
Returns:
- resp: server response if successful
Note that if the server refuses the article an exception is raised.
last(self)
Process a LAST command.  No arguments.  Return as for STAT.
list(self, group_pattern=None, *, file=None)
Process a LIST or LIST ACTIVE command. Arguments:
- group_pattern: a pattern indicating which groups to query
- file: Filename string or file object to store the result in
Returns:
- resp: server response if successful
- list: list of (group, last, first, flag) (strings)
login(self, user=None, password=None, usenetrc=True)
newgroups(self, date, *, file=None)
Process a NEWGROUPS command.  Arguments:
- date: a date or datetime object
Return:
- resp: server response if successful
- list: list of newsgroup names
newnews(self, group, date, *, file=None)
Process a NEWNEWS command.  Arguments:
- group: group name or '*'
- date: a date or datetime object
Return:
- resp: server response if successful
- list: list of message ids
next(self)
Process a NEXT command.  No arguments.  Return as for STAT.
over(self, message_spec, *, file=None)
Process an OVER command.  If the command isn't supported, fall
back to XOVER. Arguments:
- message_spec:
    - either a message id, indicating the article to fetch
      information about
    - or a (start, end) tuple, indicating a range of article numbers;
      if end is None, information up to the newest message will be
      retrieved
    - or None, indicating the current article number must be used
- file: Filename string or file object to store the result in
Returns:
- resp: server response if successful
- list: list of dicts containing the response fields
 
NOTE: the "message id" form isn't supported by XOVER
post(self, data)
Process a POST command.  Arguments:
- data: bytes object, iterable or file containing the article
Returns:
- resp: server response if successful
quit(self)
Process a QUIT command and close the socket.  Returns:
- resp: server response if successful
set_debuglevel(self, level)
Set the debugging level.  Argument 'level' means:
0: no debugging output (default)
1: print commands and responses but not body text etc.
2: also print raw lines read and sent before stripping CR/LF
slave(self)
Process a SLAVE command.  Returns:
- resp: server response if successful
starttls(self, context=None)
Process a STARTTLS command. Arguments:
- context: SSL context to use for the encrypted connection
stat(self, message_spec=None)
Process a STAT command.  Argument:
- message_spec: article number or message id (if not specified,
  the current article is selected)
Returns:
- resp: server response if successful
- art_num: the article number
- message_id: the message id
xhdr(self, hdr, str, *, file=None)
Process an XHDR command (optional server extension).  Arguments:
- hdr: the header type (e.g. 'subject')
- str: an article nr, a message id, or a range nr1-nr2
- file: Filename string or file object to store the result in
Returns:
- resp: server response if successful
- list: list of (nr, value) strings
xover(self, start, end, *, file=None)
Process an XOVER command (optional server extension) Arguments:
- start: start of range
- end: end of range
- file: Filename string or file object to store the result in
Returns:
- resp: server response if successful
- list: list of dicts containing the response fields
