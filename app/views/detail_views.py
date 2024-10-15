from flask import Blueprint, render_template, redirect, url_for, session, flash
from app.models import Post
from app import db
from flask import Blueprint, render_template, redirect, url_for, session, flash, jsonify  # jsonify 추가


bp = Blueprint('detail', __name__, url_prefix='/')


@bp.route('/detail/<int:post_id>')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    print("-----------------------------------------Image Filenames:", post.image_filename)
    return render_template('front/detail.html', post=post)


@bp.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # 로그인한 사용자와 게시글 작성자가 같은지 확인
    if post.user_id != session.get('user_id'):
        return '', 403  # 삭제 권한이 없을 경우 403 Forbidden 응답

    try:
        # 게시글 삭제
        db.session.delete(post)
        db.session.commit()
        return '', 204  # 성공적으로 삭제되었음을 알리는 204 No Content 응답
    except Exception as e:
        db.session.rollback()
        return '', 500  # 서버 오류가 발생했음을 알리는 500 Internal Server Error 응답


