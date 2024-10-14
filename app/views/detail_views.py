from flask import Blueprint, render_template
from app.models import Post

bp = Blueprint('detail', __name__, url_prefix='/')

@bp.route('/detail/<int:post_id>')  # 각 게시글의 ID를 받아서 해당 게시글 상세 보기
def detail(post_id):
    post = Post.query.get_or_404(post_id)  # 주어진 post_id에 해당하는 게시글 가져오기
    return render_template('front/detail.html', post=post)  # 게시글 데이터를 템플릿에 전달
