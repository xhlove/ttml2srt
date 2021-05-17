import glob
from xml.etree import ElementTree


def generate(path: str, out_path: str):
    '''
    首先获取到div节点 作为插入节点
    然后获取除第一个div所在xml外的其余xml的p节点 插入
    '''
    # xml 有关预设
    xmlns = 'http://www.w3.org/ns/ttml'
    ElementTree.register_namespace('', xmlns)
    # 遍历全部xml 最好是按顺序
    tree = None
    insert_node = None
    for file_path in glob.glob(path + '/*.xml'):
        _tree = ElementTree.parse(file_path)
        for node_div in _tree.getroot().iter(f'{{{xmlns}}}div'):
            if insert_node is None:
                insert_node = node_div
                tree = _tree
                continue
            node_ps = node_div.findall(f'{{{xmlns}}}p')
            insert_node.extend(node_ps)
    if tree and insert_node:
        tree.write(out_path, encoding='utf-8', short_empty_elements=False)

if __name__ == '__main__':
    generate('xmls')