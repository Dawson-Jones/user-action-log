from base import user_log_collection


def query_db(start_time=None, end_time=None, pd_no=None):
    context = dict()
    if start_time:
        context['time'] = dict()
        context['time']['$gt'] = start_time
    if end_time:
        if context.get('time') is None:
            context['time'] = dict()
        context['time']['$lte'] = end_time
    if pd_no:
        context['el_no'] = pd_no
    print(context)
    res = user_log_collection.find(context, {'_id': 0})
    num = user_log_collection.count_documents(context)
    return res, num


if __name__ == '__main__':
    res, _ = query_db()
    print(res[0])
